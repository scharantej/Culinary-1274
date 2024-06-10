## Flask Application Design

### HTML Files

- **index.html:** The primary page of the website, displaying the culinary arts course curriculum and providing navigation to other pages.
- **lessons.html:** A single-page to show a list of all lessons.
- **lesson_detail.html:** A single-page to show the content of a selected lesson.

### Routes
#### Main Page
- **route:** `/`
- **method:** GET
- **purpose:** Display the index page with the course curriculum.

#### Lessons
- **route:** `/lessons`
- **method:** GET
- **purpose:** Display a list of all lessons.

#### Individual Lesson
- **route:** `/lesson/<lesson_id>`
- **method:** GET
- **purpose:** Display the content of the selected lesson.