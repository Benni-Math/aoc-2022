// Import Node helpers
import fs from 'fs';

// Import constants
import INPUT_FILES from './constants/INPUT_FILES';

// Import day solutions
import days from './days';

const main = async () => {
  // const IO = Promise.resolve();
  // INPUT_FILES.forEach((inputFilename, day) => {
  //   days[day].forEach((solnFunc, part) => {
  //     IO
  //       .then(() => solnFunc(inputFilename))
  //       .then((answer) => console.log(`Day ${day + 1}, pt${part + 1}: ${answer}`));
  //   });
  // });

  const daySolutions = days.slice(0, fs.readdirSync('../inputs/').length);

  const answers = await Promise.all(
    daySolutions.map(
      (parts, day) => Promise.all(
        parts.map((solnFunc) => solnFunc(INPUT_FILES[day])),
      ),
    ),
  );

  answers.forEach(
    (dayAnswers, day) => {
      console.log(`Day ${day + 1}:`);
      dayAnswers.forEach(
        (answer, part) => console.log(`  Part ${part + 1}: ${answer}`),
      );
      console.log('');
    },
  );
};

if (require.main === module) {
  main();
}
