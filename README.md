# UniReq
### Introduction:

UniReq is an online platform that aims to provide students with easy access to International Baccalaureate (IB) requirements for various universities and courses. The platform will utilize networking features and a database to ensure that users can easily search and find the admission criteria for their desired course and university.

### Features:

UniReq will have the following features:

1. Search functionality: Users can search by country, university, and course to find the admission criteria, including minimum scores, subject requirements, and language proficiency.
2. User details: Users can give their score and recieve the best university ranking based on the user’s score.
3. Feedback: Users can provide feedback on the accuracy of the admission criteria listed on the platform.

### Technical details:

UniReq will be developed using the `Flask web framework`. The user can search all their desired information, which will all be stored on a database, mostly using `SQLLITE` or `SQL`. Using the a web framework users can get access to any details, formated clean and simplistic. If there are any inconsistencies with the data, the user can submit a feedback which will be added to the database.

### Conclusion:

UniReq will provide a valuable service to students seeking admission to universities offering IB courses. The platform's search functionality and user accounts will ensure that users can easily find. The feedback feature will also ensure that the admission criteria listed on the platform are accurate and up-to-date. Overall, UniReq has the potential to simplify the university admission process for IB students.

---
**Table: Countries**

- country_id (Primary Key)
- name

| Country ID | Country Name |
| --- | --- |
|  |  |
|  |  |

**Table: Universities**

- university_id (Primary Key)
- name
- country_id (Foreign Key referencing Countries.country_id)

| Universities ID | University Name | Country ID |
| --- | --- | --- |
|  |  |  |
|  |  |  |

**Table: Courses**

- course_id (Primary Key)
- name
- university_id (Foreign Key referencing Universities.university_id)

| Course ID | Course Name | University ID |
| --- | --- | --- |
|  |  |  |
|  |  |  |

**Table: AdmissionCriteria**

- admission_criteria_id (Primary Key)
- course_id (Foreign Key referencing Courses.course_id)
- IB_Score
- subject_requirements
- language_proficiency

| Admission Criteria ID | Course ID | IB_Score | Subject Requirements | Language Proficiency |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |

**Table: Feedback**

- feedback_id (Primary Key)
- feedback_text

| Feedback ID | Feedback |
| --- | --- |
|  |  |
|  |  |

## All Dependency
- Flask
- Jinja2
- Werkzeug
- SQLAlchemy
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login

## Running the Website
Before you can rush in, confirm you have Python 3.11.xx (I have 3.11.3) and all the dependency are in the virtualenviroment. 
Next create the tables in the terminal, or if you are lazy, run the app.py two times (the data will duplicate, if you don't care) and the server is up. Copy the localhost and enjoy
PS: Username: admin Password: admin

