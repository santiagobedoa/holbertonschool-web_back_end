const fs = require('fs');

const countStudents = (aPath) => new Promise((resolve, reject) => {
  fs.readFile(aPath, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    let lines = data.trim().split('\n');
    lines = lines.slice(1, lines.length);
    console.log(`Number of students: ${lines.length}`);
    const courses = {};
    for (const row of lines) {
      const student = row.split(',');
      if (!courses[student[3]]) courses[student[3]] = [];
      courses[student[3]].push(student[0]);
    }
    for (const course in courses) {
      if (course) {
        console.log(
          `Number of students in ${course}: ${
            courses[course].length
          }. List: ${courses[course].join(', ')}`,
        );
      }
    }
    resolve();
  });
});

module.exports = countStudents;
