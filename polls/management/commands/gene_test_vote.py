import datetime
import random

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from polls.models import Questionnaire, Question, Choice, VoteRecord


def random_votes(random_times, num_vote_types):
    votes_list = [0] * num_vote_types
    for i in range(random_times):
        votes_list[random.randint(0, num_vote_types-1)] += 1
    return votes_list

class Command(BaseCommand):
    help = 'Generate vote data for test'

    def add_arguments(self, parser):
        parser.add_argument('gene_type', type=str)

    def handle(self, *args, **options):
        if options['gene_type'] == "vote":
            vote_times= 100
            for questionnaire in Questionnaire.objects.all():
                for question in questionnaire.question_set.all():
                    votes_list = random_votes(vote_times, question.choice_set.count())
                    for i, choice in enumerate(question.choice_set.all()):
                        choice.votes += votes_list[i]
                        choice.save()
        if options['gene_type'] == "vote_record":
            record_nums = 300
            for i in range(record_nums):
                vote_date = timezone.now() - datetime.timedelta(minutes=random.randint(1,14*24*60))
                ip_address = ":".join([str(random.randint(1,255)) for i in range(4)])
                questionnaire_id = random.randint(1,Questionnaire.objects.count())
                vote_record = VoteRecord(vote_date=vote_date, ip_address=ip_address, 
                                        questionnaire_id=questionnaire_id)
                vote_record.save()


