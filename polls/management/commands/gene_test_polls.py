import datetime
import random

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from polls.models import Questionnaire, Question, Choice, VoteRecord


class Command(BaseCommand):
    help = 'Generate polls for test'

    def add_arguments(self, parser):
        parser.add_argument('--gene_num', type=int, default=20)

    def handle(self, *args, **options):
        # delete Questionnaire.objects.filter(id__gt=3).delete()
        # reset index ALTER TABLE table_name AUTO_INCREMENT = 1;
        gene_time = options['gene_num']
        origin_count = Questionnaire.objects.count()
        for i in range(gene_time):
            polls_orders = origin_count + i + 1
            print(polls_orders)
            pub_date = timezone.now() - datetime.timedelta(days=(400-i))
            questionnaire = Questionnaire(questionnaire_name="测试问卷{}".format(polls_orders), 
                                        pub_date=pub_date,
                                        detail_info="用于测试的问卷")
            questionnaire.save()
            for j in range(4):
                question = Question(question_text="测试问题{}".format(j+1),
                                    question_type=1,
                                    questionnaire=questionnaire)
                question.save()
                for k in range(4):
                    choice = Choice(choice_text="测试选项{}".format(k+1),
                    votes=random.randint(50,200),
                    question=question)
                    choice.save()

            self.stdout.write(self.style.SUCCESS('Successfully generate test questionnaire'))
