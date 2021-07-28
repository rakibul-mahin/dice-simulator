#------------ LIBRARIES ------------#
import random
#------------ LIBRARIES ------------#

#------------ PROJECT TITLE ------------#
print("Project-1 | DICE SIMULATOR")
#------------ PROJECT TITLE ------------#

#------------ DICE SIMULATOR ------------#

#GENERATING RANDOM NUMBER FOR OUR DICE
dice_number = random.randint(1,6)

#NAIN CODE, FOR PRINTING DICE WITH NUMBER
if dice_number == 1:
    print('---------------')
    print('|             |')
    print('|             |')
    print('|      *      |')
    print('|             |')
    print('|             |')
    print('---------------')
elif dice_number == 2:
    print('---------------')
    print('|          *  |')
    print('|             |')
    print('|             |')
    print('|             |')
    print('|   *         |')
    print('---------------')
elif dice_number == 3:
    print('---------------')
    print('|          *  |')
    print('|             |')
    print('|       *     |')
    print('|             |')
    print('|   *         |')
    print('---------------')
elif dice_number == 4:
    print('---------------')
    print('|             |')
    print('|   *      *  |')
    print('|             |')
    print('|   *      *  |')
    print('|             |')
    print('---------------')
elif dice_number == 5:
    print('---------------')
    print('|             |')
    print('|  *      *   |')
    print('|      *      |')
    print('|  *      *   |')
    print('|             |')
    print('---------------')
elif dice_number == 6:
    print('---------------')
    print('|  *       *  |')
    print('|             |')
    print('|  *       *  |')
    print('|             |')
    print('|  *       *  |')
    print('---------------')

#------------ DICE SIMULATOR ------------#