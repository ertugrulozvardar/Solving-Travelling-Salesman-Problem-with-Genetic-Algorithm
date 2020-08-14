from RouteManager import RouteManager
from Route import Route

import numpy as np
import random as random

class GeneticAlgorithmSolver:
    def __init__(self, cities, population_size=50, mutation_rate=0.2, tournament_size=10, elitism=False):
        self.cities = cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elitism = elitism

    def evolve(self, routes):
        # YOUR CODE HERE
    
        new_routes = RouteManager(self.cities, routes.population_size)
        offSet = 0
        if self.elitism:
            new_routes.set_route(0, routes.find_best_route())
            offSet = 1
        
        for k in range(offSet, routes.population_size):
            proute_1 = self.tournament(routes)
            proute_2 = self.tournament(routes)

            child = self.crossover(proute_1, proute_2) # Crossing-over of two parent routes.
            new_routes.set_route(k, child)
        
        for k in range(offSet, routes.population_size):
            self.mutate(new_routes.get_route(k))       # Mutation 
        
        return new_routes


    def crossover(self, route_1, route_2):
         # YOUR CODE HERE

        child = Route(self.cities)
        initial_State = int(random.random() * len(route_1))
        final_State = int(random.random() * len(route_1))
            
        for k in range(0, len(child)):
            if (initial_State < final_State and k > initial_State and k < final_State):
                child.assign_city(k, route_1.get_city(k))
            elif initial_State > final_State:
                if not (k < initial_State and k > final_State):
                    child.assign_city(k, route_1.get_city(k))
            
        for k in range(0, len(route_2)):
            if not child.__contains__(route_2.get_city(k)):
                for m in range(0, len(child)):
                    if (child.get_city(m) == None):
                        child.assign_city(m, route_2.get_city(k))
                        break
            
        return child

    def mutate(self, route):
        # YOUR CODE HERE
         for route_State_1 in range(0, len(route)):
            if (random.random() < self.mutation_rate):
                route_State_2 = int(len(route) * random.random())
                
                city_1 = route.get_city(route_State_1)
                city_2 = route.get_city(route_State_2)
                
                #Swapping operations
                route.assign_city(route_State_2, city_1)
                route.assign_city(route_State_1, city_2)

    def tournament(self, routes):
         # YOUR CODE HERE
        tournament = RouteManager(self.cities, self.tournament_size)

        for k in range(0, self.tournament_size):
            random_n = int(random.random() * routes.population_size)
            tournament.set_route(k, routes.get_route(random_n))
        best_route = tournament.find_best_route()     
        return best_route
