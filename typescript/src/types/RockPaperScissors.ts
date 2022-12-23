/**
 * Type describing a round of rock-paper-scissors,
 * as defined in AOC-2022 day 2.
 * @author Benedikt Arnarsson
 */
namespace RockPaperScissors {
  type Player1 = 'A' | 'B' | 'C';
  type Player2 = 'X' | 'Y' | 'Z';
  export type GameStr = `${Player1} ${Player2}`;

  type RPS = 1 | 2 | 3; // Rock | Paper | Scissors
  export type Game = [RPS, RPS];

  /**
   * Changes a GameStr into it's Game representation.
   * @author Benedikt Arnarsson
   * @param game the string representing the game, defined by AOC day 2.
   * @returns Internal type representing a rock-paper-scissors game.
   * 1 = Rock, 2 = Paper, 3 = Scissors.
   */
  export const fromString = (game: GameStr): Game => {
    if (game.length !== 3 || game[1] !== ' ') {
      throw new Error(`Malformed game: ${game}`);
    }
    // Could add some input verification...
    const [player1, player2] = game.split(' ');

    const player1Code = player1.charCodeAt(0);
    if (player1Code > 67 && player1Code < 65) {
      throw new Error(`Malformed game: ${game}`);
    }

    const player2Code = player2.charCodeAt(0);
    if (player2Code > 90 || player2Code < 88) {
      throw new Error(`Malformed game: ${game}`);
    }

    return [player1Code - 64, player2Code - 87] as Game;
  };

  /**
   * Provides the score for Player2.
   * Score defined by day 2 of AoC.
   * @author Benedikt Arnarsson
   * @param game The game to be played [Player1, Player2]
   * @returns Player2's score
   */
  export const score = (game: Game): number => {
    const [player1Pt, player2Pt] = game;

    let totalPts = player2Pt;
    if (player1Pt === player2Pt) totalPts += 3;
    if ((player2Pt - player1Pt) % 3 === 1) totalPts += 6;

    return totalPts;
  };
}

export default RockPaperScissors;
