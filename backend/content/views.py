from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

from pypdf import PdfReader

from .models import ContentSource, ContentDocument, ContentChunk
from .serializers import ContentUploadSerializer, ContentChunkSerializer
from syllabus.models import Subtopic

# Create your views here.

class ContentUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ContentUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data["file"]
        subtopic = Subtopic.objects.get(id=serializer.validated_data["subtopic_id"])

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

        # Extract text
        reader = PdfReader(document.file)
        full_text = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

        document.extracted_text = full_text
        document.processed = True
        document.save()

        # Chunk text (simple paragraph-based chunking)
        paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]

        for para in paragraphs:
            ContentChunk.objects.create(
                document=document,
                subtopic=subtopic,
                topic=subtopic.topic,
                subject=subtopic.topic.subject,
                text=para[:2000],  # safety limit
            )

        return Response(
            {"message": "Content uploaded and processed successfully."},
            status=status.HTTP_201_CREATED,
        )


class SubtopicNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, subtopic_id):
        chunks = ContentChunk.objects.filter(
            subtopic_id=subtopic_id,
            document__uploaded_by=request.user,
        )

        serializer = ContentChunkSerializer(chunks, many=True)
        return Response(serializer.data)