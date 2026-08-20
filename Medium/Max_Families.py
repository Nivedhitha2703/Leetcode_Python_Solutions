class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        answer = (n - len(rows)) * 2

        # Check rows that have reserved seats
        for seats in rows.values():
            count = 0

            # Seats 2,3,4,5
            if all(seat not in seats for seat in [2, 3, 4, 5]):
                count += 1

            # Seats 6,7,8,9
            if all(seat not in seats for seat in [6, 7, 8, 9]):
                count += 1

            # If neither outer block is available,
            # check the middle block 4,5,6,7
            if count == 0:
                if all(seat not in seats for seat in [4, 5, 6, 7]):
                    count = 1

            answer += count

        return answer
