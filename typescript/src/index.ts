// Import constants
import INPUT_FILES from './constants/INPUT_FILES';

// Import day solutions
import days from './days';

const main = async () => {
  const IO = Promise.resolve();
  INPUT_FILES.forEach((inputFilename, day) => {
    days[day].forEach((solnFunc, part) => {
      IO
        .then(() => solnFunc(inputFilename))
        .then((answer) => console.log(`Day ${day + 1}, pt${part + 1}: ${answer}`));
    });
  });

  // const answers = await Promise.all(
  //   INPUT_FILES.map(
  //     (inputFilename, day) => Promise.all(
  //       days[day].map((solnFunc) => solnFunc(inputFilename)),
  //     ),
  //   ),
  // );

  // answers.forEach(
  //   (dayAnswers, day) => dayAnswers.forEach(
  //     (answer, part) => console.log(`Day ${day + 1}, pt${part + 1}: ${answer}`),
  //   ),
  // );
};

if (require.main === module) {
  main();
}
