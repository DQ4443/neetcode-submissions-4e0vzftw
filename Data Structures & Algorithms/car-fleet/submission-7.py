class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # can keep a stack of fleets, based on time arrive.
        # need to sort by position first. use zip
        # compare each car's time against the current stack head. if faster, pop the car since it will arrive
        # return length of the stack

        # T = D / S

        cars = sorted(zip(position, speed), reverse=True)

        fleets = []

        for car in cars:
            distance = target - car[0]
            v = car[1]
            time = distance / v

            if not fleets or time > fleets[-1]:
                fleets.append(time)


        return len(fleets)
