import csv
from django.core.management.base import BaseCommand
from main.models import School, AssessmentAreas, Awards, Class, Subject, Answers, Student, Summary

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('csv_files', nargs='+', type=str, help='Paths to CSV files')

    def handle(self, *args, **kwargs):
        csv_files = kwargs['csv_files']

        for csv_file in csv_files:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                batch_size = 1000  
                batch = []

                for row in reader:
                    school, _ = School.objects.get_or_create(Name=row['school_name'])
                    assessment_area, _ = AssessmentAreas.objects.get_or_create(Name=row['Assessment Areas'])
                    award, _ = Awards.objects.get_or_create(Name=row['award'])
                    class_obj, _ = Class.objects.get_or_create(ClassName=row['Class'])
                    subject, _ = Subject.objects.get_or_create(SubjectName=row['Subject'])
                    answers, _ = Answers.objects.get_or_create(Answer=row['Answers'])
                    student_name = f"{row['First Name']} {row['Last Name']}"
                    student, _ = Student.objects.get_or_create(Name=student_name, Class=class_obj, School=school)
                    
                    summary = Summary(
                        School=school,
                        SydneyParticipant=row['sydney_participants'],
                        SydneyPercentile=row['sydney_percentile'],
                        AssessmentArea=assessment_area,
                        Award=award,
                        Class=class_obj,
                        CorrectAnswerPercentagePerClass=row['correct_answer_percentage_per_class'],
                        CorrectAnswer=answers,
                        Student=student,
                        Participant=row['participant'],
                        StudentScore=row['student_score'],
                        Subject=subject,
                        YearLevelName=row['Year Level'],
                        Answer=answers
                    )
                    batch.append(summary)

                    if len(batch) >= batch_size:
                        Summary.objects.bulk_create(batch)
                        batch = []

                
                if batch:
                    Summary.objects.bulk_create(batch)

        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV files'))
