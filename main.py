import argparse
import database_operations


def main():
    parser = argparse.ArgumentParser(description='CRUD Operations with Database Models')
    parser.add_argument('--action', '-a', choices=['create', 'list', 'update', 'remove'], required=True,
                        help='CRUD action')
    parser.add_argument('--model', '-m', choices=['Student', 'Group', 'Lecturer', 'Subject', 'Grades'], required=True,
                        help='Database model')
    parser.add_argument('--id', type=int, help='ID of the record')
    parser.add_argument('--name', help='Name for creating or updating records')
    parser.add_argument('--last_name', help='Last name for creating or updating records')
    parser.add_argument('--group_id', help='Group id for creating or updating records')
    parser.add_argument('--mark')
    parser.add_argument('--exam_date')
    parser.add_argument('--subject_id')
    parser.add_argument('--student_id')
    parser.add_argument('--lecturer_id')

    args = parser.parse_args()

    if args.action == 'create':
        if args.model == 'Student':
            database_operations.create_student(args.name, args.last_name, args.group_id)
        elif args.model == 'Group':
            database_operations.create_group(args.name)
        elif args.model == 'Lecturer':
            database_operations.create_lecturer(args.name, args.last_name)
        elif args.model == 'Subject':
            database_operations.create_subject(args.name, args.lecturer_id)
        elif args.model == 'Grades':
            database_operations.create_grade(args.student_id, args.subject_id, args.mark, args.exam_date)
        else:
            print(f"Invalid model: {args.model}")

    elif args.action == 'list':
        if args.model == 'Student':
            database_operations.list_students()
        elif args.model == 'Group':
            database_operations.list_groups()
        elif args.model == 'Lecturer':
            database_operations.list_lecturers()
        elif args.model == 'Subject':
            database_operations.list_subjects()
        elif args.model == 'Grades':
            database_operations.list_grades()
        else:
            print(f"Invalid model: {args.model}")

    elif args.action == 'update':
        if args.model == 'Student':
            database_operations.update_student(args.id, args.name, args.last_name, args.group_id)
        elif args.model == 'Group':
            database_operations.update_group(args.id, args.name)
        elif args.model == 'Lecturer':
            database_operations.update_lecturer(args.id, args.name, args.last_name)
        elif args.model == 'Subject':
            database_operations.update_subject(args.id, args.name, args.lecturer_id)
        elif args.model == 'Grades':
            database_operations.update_grade(args.id, args.new_student_id, args.new_subject_id, args.new_mark,
                                             args.new_exam_date)
        else:
            print(f"Invalid model: {args.model}")

    elif args.action == 'remove':
        if args.model == 'Student':
            database_operations.remove_student(args.id)
        elif args.model == 'Group':
            database_operations.remove_group(args.id)
        elif args.model == 'Lecturer':
            database_operations.remove_lecturer(args.id)
        elif args.model == 'Subject':
            database_operations.remove_subject(args.id)
        elif args.model == 'Grades':
            database_operations.remove_grade(args.id)
        else:
            print(f"Invalid model: {args.model}")

    else:
        print(f"Invalid action: {args.action}")

    database_operations.close_session()


if __name__ == "__main__":
    main()
