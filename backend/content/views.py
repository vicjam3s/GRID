from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from pypdf import PdfReader

from .models import ContentSource, ContentDocument, ContentChunk
from .serializers import ContentUploadSerializer, ContentChunkSerializer
from syllabus.models import Subject, Topic


class ContentUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ContentUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data["file"]
        subject_id = serializer.validated_data.get("subject_id")
        topic_id = serializer.validated_data.get("topic_id")

        subject = None
        topic = None

        if subject_id:
            subject = Subject.objects.get(id=subject_id)

        if topic_id:
            topic = Topic.objects.get(id=topic_id)

        # Create content source
        source = ContentSource.objects.create(
            title=file.name,
            source_type="USER_UPLOAD",
        )

        document = ContentDocument.objects.create(
            source=source,
            uploaded_by=request.user,
            file=file,
        )

        # Extract text from PDF
        reader = PdfReader(document.file)
        full_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

        document.extracted_text = full_text
        document.processed = True
        document.save()

        # Chunk text (paragraph-based)
        paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]

        for para in paragraphs:
            ContentChunk.objects.create(
                document=document,
                subject=subject,
                topic=topic,
                text=para[:2000],
            )

        return Response(
            {"message": "Content uploaded and processed successfully."},
            status=status.HTTP_201_CREATED,
        )


class TopicNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        topic_id = request.GET.get("topic")

        chunks = ContentChunk.objects.filter(
            topic_id=topic_id,
            document__uploaded_by=request.user,
        )

        serializer = ContentChunkSerializer(chunks, many=True)
        return Response(serializer.data)