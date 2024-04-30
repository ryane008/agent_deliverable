import random
from agent import Agent
from parallel_utils import Parallel_Utils
import matplotlib.pyplot as plt

def create_agents(i):
    new_agent = Agent(i)
    return new_agent

def initialize_stats(agent: Agent):
    return {agent.id: {0: (agent.energy,-1)}}

def visualize_results(agent_tracking: list, ids: list = None):
    if ids is None:
        for i in range(len(agent_tracking[0][0])):
            agents = []
            energies = []
            
            for index, val in enumerate(agent_tracking):
                agents.append(index)
                energies.append(val[index][i][0])
                
            fig = plt.figure(figsize = (10, 5))
            plt.bar(agents, energies, color ='maroon', 
                    width = 0.4)
            plt.xlabel("Agents")
            plt.ylabel("Energies")
            plt.title(f"Energies of Agents at Round {i}")
            plt.show()   
    else:
        for id in ids:
            rounds = []
            energies = []
            for key, val in agent_tracking[id].items():
                rounds.append[key]
                energies.append[val]
            round_count = len(rounds) - 1
            plt.plot(rounds, energies, marker='o', linestyle='-')
            plt.xlabel('Interaction Round')
            plt.ylabel('Energy Values')
            plt.title(f'Energy of agent {id} after {round_count} rounds')
            plt.show()
    
def print_result(ids: list[int], agent_tracking:list):
    for id in ids:
        print(f"Stats for Agent {id}")
        print("--------------------------")
        round_data = agent_tracking[id][id]
        for round, val in round_data.items():
            print(f"Round {round}: ")
            print("Energy: ", val[0])
            print("Agent Counterpart id: ", val[1])
        print("--------------------------")

def interaction_round(agents: list[Agent], round: int, agent_tracking: list):
    for agent in agents:
        other_agent_index = random.randint(0, 99)
        other_agent = agents[other_agent_index]
        if agent.energy > other_agent.energy:
            energy_transfer(agent, other_agent)
            agent_tracking[agent.id][agent.id][round] = (agent.energy, other_agent.id)
        else:
            energy_transfer(other_agent, agent)
            agent_tracking[agent.id][agent.id][round] = (agent.energy, other_agent.id)
        
            
#agent_one will always be higher based on interaction round
def energy_transfer(agent_one: Agent, agent_two: Agent):
    prob = random.randint(0, 3)
    
    #lower probability for agent with lower energy (1/4)
    if prob == 0:
        if "integer" in agent_two.transfer_type.keys(): 
            if agent_one.energy < agent_two.transfer_type["integer"] or (agent_two.energy + agent_two.transfer_type["integer"]) > 150:
                return
            else:
                agent_one.setEnergy(agent_two.transfer_type["integer"], False)
                agent_two.setEnergy(agent_two.transfer_type["integer"], True)
        else:
            val = agent_two.transfer_type["percentage"] * agent_one.energy
            if agent_one.energy < val or agent_two.energy + val > 150:
                return
            else:
                agent_one.setEnergy(val, False)
                agent_two.setEnergy(val, True)
    else:
        if "integer" in agent_one.transfer_type.keys(): 
            if agent_two.energy < agent_one.transfer_type["integer"] or (agent_one.energy + agent_one.transfer_type["integer"]) > 150:
                return
            else:
                agent_one.setEnergy(agent_one.transfer_type["integer"], True)
                agent_two.setEnergy(agent_one.transfer_type["integer"], False)
        else:
            val = agent_one.transfer_type["percentage"] * agent_two.energy
            if agent_two.energy < val or agent_one.energy + val > 150:
                return
            else:
                agent_one.setEnergy(val, True)
                agent_two.setEnergy(val, False)

def main():
    #list of agents
    agents = []
    
    #structure: [{agent_id : {round_number : [energy_after_round, other_agent]}}]
    #agent tracking is the history of each agent at a given round
    agent_tracking = {}
    
    args_list = list(range(100))
    agents = Parallel_Utils.run_process(create_agents, args_list=args_list)
    
    #initializing data tracking
    agent_tracking = Parallel_Utils.run_process(initialize_stats, agents)
    for i in range(1, 6):
        interaction_round(agents, i, agent_tracking)
    
    visualize_results(agent_tracking)
    print_result([0, 30, 81, 99], agent_tracking)
    
if __name__ == '__main__':
    main()





