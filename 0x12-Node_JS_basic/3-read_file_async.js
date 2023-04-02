const fs = require("fs");

const countStudents = (aPath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(aPath, "utf8", (err, data) => {
      if (err) {
        reject(new Error("Cannot load the database"));
        return;
      }

      const lines = data.trim().split("\n");
      const headers = lines[0].split(",");
      const students = lines
        .slice(1)
        .filter((line) => line.trim() !== "")
        .map((line) => {
          const values = line.split(",");
          return headers.reduce((obj, header, i) => {
            obj[header] = values[i];
            return obj;
          }, {});
        });

      const courses = {};
      students.forEach((student) => {
        const course = student["field"];
        if (!courses[course]) courses[course] = [];
        courses[course].push(student["firstname"]);
      });

      console.log(`Number of students: ${students.length}`);
      for (const course in courses) {
        console.log(
          `Number of students in ${course}: ${
            courses[course].length
          }. List: ${courses[course].join(", ")}`
        );
      }
      resolve();
    });
  });
};

module.exports = countStudents;
