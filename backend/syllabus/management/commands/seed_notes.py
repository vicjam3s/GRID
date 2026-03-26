# from django.core.management.base import BaseCommand
# from syllabus.models import Note, Subtopic

# from knowledge_base.PPL.AL.notes import NOTES as AL_NOTES
# from knowledge_base.PPL.OPS.notes import NOTES as OPS_NOTES
# # from knowledge_base.PPL.HP.notes import NOTES as HP_NOTES
# # from knowledge_base.PPL.ACP.notes import NOTES as ACP_NOTES
# # from knowledge_base.PPL.FP.notes import NOTES as FP_NOTES
# # from knowledge_base.PPL.MB.notes import NOTES as MB_NOTES
# # from knowledge_base.PPL.AF.notes import NOTES as AF_NOTES
# # from knowledge_base.PPL.MET.notes import NOTES as MET_NOTES
# # from knowledge_base.PPL.POF.notes import NOTES as POF_NOTES
# # from knowledge_base.PPL.COMM.notes import NOTES as COMM_NOTES
# # from knowledge_base.PPL.INS.notes import NOTES as INS_NOTES
# # from knowledge_base.PPL.DC.notes import NOTES as DC_NOTES


# class Command(BaseCommand):

#     help = "Seed notes from knowledge_base"

#     def handle(self, *args, **kwargs):

#         all_notes = (
#             AL_NOTES
#             + OPS_NOTES
#             # + HP_NOTES
#             # + ACP_NOTES
#             # + FP_NOTES
#             # + MB_NOTES
#             # + AF_NOTES
#             # + MET_NOTES
#             # + POF_NOTES
#             # + COMM_NOTES
#             # + INS_NOTES
#             # + DC_NOTES
#         )

#         for note in all_notes:

#             subtopic = Subtopic.objects.filter(title=note["subtopic"]).first()

#             if not subtopic:
#                 self.stdout.write(
#                     self.style.WARNING(f"Subtopic not found: {note['subtopic']}")
#                 )
#                 continue

#             Note.objects.update_or_create(

#                 subtopic=subtopic,
#                 title=note["title"],

#                 defaults={
#                     "content": note["content"]
#                 }
#             )

#         self.stdout.write(self.style.SUCCESS("Notes seeded successfully."))