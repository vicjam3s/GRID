from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NotePDF


class NotesBySubjectView(APIView):

    def get(self, request):
        subject = request.GET.get("subject")

        notes = NotePDF.objects.filter(subject=subject)

        data = [
            {
                "title": note.title,
                "file": request.build_absolute_uri(note.file.url)
            }
            for note in notes
        ]

        return Response(data)