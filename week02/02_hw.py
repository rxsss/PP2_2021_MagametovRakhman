class Solution:
    def interpret(self, command: str) -> str:
        goal = ''
        for i in range(len(command)):
            if command[i] == "G":
                goal = goal + 'G'
            elif command[i] == "(":
                if command[i+1] == ")":
                    goal = goal + 'o'
                elif command[i+1] == "a":
                    if command[i+2] == "l":
                        if command[i+3] == ")":
                            goal = goal + 'al'
        return goal