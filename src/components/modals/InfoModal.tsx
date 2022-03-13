import { Cell } from '../grid/Cell'
import { BaseModal } from './BaseModal'

type Props = {
  isOpen: boolean
  handleClose: () => void
}

export const InfoModal = ({ isOpen, handleClose }: Props) => {
  return (
    <BaseModal title="How to play" isOpen={isOpen} handleClose={handleClose}>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        In Bibble, try to guess the word from the King James V Bible.
        Guess the word in 10 tries. After each guess, the color of the tiles will
        change to show how close your guess was to the word.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell
          isRevealing={true}
          isCompleted={true}
          value="P"
          status="correct"
        />
        <Cell value="O" />
        <Cell value="P" />
        <Cell value="U" />
        <Cell value="L" />
        <Cell value="A" />
        <Cell value="R" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        The letter P is in the word and in the correct spot.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="C" />
        <Cell value="O" />
        <Cell
          isRevealing={true}
          isCompleted={true}
          value="R"
          status="present"
        />
        <Cell value="O" />
        <Cell value="N" />
        <Cell value="E" />
        <Cell value="R" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        The letter R is in the word but in the wrong spot.
      </p>

      <div className="flex justify-center mb-1 mt-4">
        <Cell value="P" />
        <Cell value="E" />
        <Cell value="T" />
        <Cell isRevealing={true} isCompleted={true} value="U" status="absent" />
        <Cell value="N" />
        <Cell value="I" />
        <Cell value="A" />
      </div>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        The letter U is not in the word in any spot.
      </p>

      <p className="mt-6 italic text-sm text-gray-500 dark:text-gray-300">
        This is an open source version of the word guessing game we all know and
        love -{' '}
        <a
          href="https://github.com/cwackerfuss/react-wordle"
          className="underline font-bold"
        >
          check out the code here
        </a>{' '}
      </p>
    </BaseModal>
  )
}
