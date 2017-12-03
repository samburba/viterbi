import numpy as np
from pandas import * #NOT import, just used to visualize table easier
class Viterbi:
    def __init__(self, initial, states, obs, possible_obs, trans, emiss):
        self.initial = initial
        self.states = states
        self.obs = obs
        self.possible_obs = possible_obs
        self.trans = trans
        self.emiss = emiss
        self.num_states = len(self.states)
        self.num_obs = len(self.obs)
        self.table = np.zeros((self.num_states, self.num_obs + 1))

    def get_obs_num(self, obs):
        return self.possible_obs.index(obs)

    def run(self):
        path = []
        #set the initial values to the start of the table
        for st in range(self.num_states):
            self.table[st][0] = self.initial[st]
        #find the value for each state at each time

        #B
        # print(self.table[0][0])
        # print(self.trans[0][0])
        # print(self.emiss[0][1])
        # print(self.table[1][0])
        # print(self.trans[0][1])
        # print(self.emiss[0][1])
        # print(self.table[2][0])
        # print(self.trans[0][2])
        # print(self.emiss[0][1])
        # print(prob)
        # #L
        # print(self.table[1][0])
        # print(self.trans[1][0])
        # print(self.emiss[1][1])
        # print(self.table[1][0])
        # print(self.trans[1][1])
        # print(self.emiss[1][1])
        # print(self.table[1][0])
        # print(self.trans[1][2])
        # print(self.emiss[1][1])
        # print(prob)
        for ob in range(self.num_obs):
            observed = self.possible_obs.index(obs[ob])
            if observed:
                print("Tails")
            else:
                print("Heads")
            for i in range(self.num_states):
                prob = []
                for j in range(self.num_states):
                    #table is wrong -.-
                    prob.append(self.table[j][ob] * self.trans[i][j] * self.emiss[i][observed])
                    print(self.table[i][ob])
                print(DataFrame(prob))
                self.table[i][ob + 1] = max(prob);

    def print_table(self):
        print( DataFrame(self.table))

if __name__ == "__main__":
    states = ["Balanced", "Loaded_Heads", "Loaded_Tails"]
    obs = ["Tails", "Tails", "Heads", "Heads", "Tails"]
    possible_obs = ["Heads", "Tails"]
    initial = [0.333, 0.333, 0.333]
    #   trans matrix follows the following pattern:
    #       [[balanced->balanced, loaded_heads->balanced, loaded_tails->balanced],
    #       [balanced->loaded_heads, loaded_heads->loaded_heads, loaded_tails->loaded_heads],
    #       [balanced->loaded_tails, loaded_heads->loaded_tails, loaded_tails->loaded_tails]]
    trans = [[0.45, 0.52, 0.25], [0.35, 0.3, 0.13], [0.2, 0.18, 0.62]]
    #   emiss matrix follows the following pattern:
    #   [[balanced->heads, balanced->tails], [loaded_heads->heads, loaded_heads->tails] ...]
    emiss = [[0.5, 0.5], [0.85, 0.15], [0.1, 0.9]]
    v = Viterbi(initial, states, obs, possible_obs, trans, emiss)
    v.run()
    v.print_table()
