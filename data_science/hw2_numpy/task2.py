import numpy as np

if __name__ == "__main__":
    indices = np.indices((8, 8))
    board = (indices[0] + indices[1]) % 2
    row3 = board[2]
    column5 = board[:,4:5]
    left_corner = board[:3, :3]

    print(f"\n--- Chess board ---\n{board}")
    print(f"\nThird row:\n{row3}")
    print(f"\nFifth column:\n{column5}")
    print(f"\nLeft corner (3x3):\n{left_corner}")