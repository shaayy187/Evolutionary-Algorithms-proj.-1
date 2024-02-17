import random
import benchmark_functions as bf

class Chromosome:
    size = None

    def __init__(self):
        # self.gene = [0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0]
        self.gene = []
        self.gene_decoded = 0

    def create_gene(self):
        for i in range(0, self.size):
            number = random.choice([0, 1])
            self.gene.append(number)
        self.update_gene()

    def set_gene(self, new_gene: list):
        self.gene = new_gene
        # self.update_gene()

    def update_gene(self):
        gene_temp = ''.join(map(str, self.gene))
        self.gene_decoded = int(gene_temp, 2)


class Individual:
    range_start = None
    range_end = None

    def __init__(self):
        self.chromosome = []  # [Chromosome1, Chromosome2]
        self.chromosome_values = []  # [value1, value2]
        self.fitness_function_value = None

    def add_chromosome(self, new_chromosome: Chromosome):
        self.chromosome.append(new_chromosome)
        # value = self.chromosome_decode(Individual.range_start, Individual.range_end, new_chromosome)
        # self.chromosome_values.append(value)

    def update_values(self):
        for chromosome in self.chromosome:
            value = self.chromosome_decode(Individual.range_start, Individual.range_end, chromosome)
            self.chromosome_values.append(value)
        self.set_fitness_function()

    def set_fitness_function(self):
        self.fitness_function_value = self.fitness_function(self.chromosome_values, Population.get_func_type())

    @staticmethod
    def fitness_function(variables: list, func_type) -> float:  # variables = [variable1, variable2, variable3]
        variables_amount = len(variables)
        match func_type:
            case 1:
                return variables[0] ** 3 - 7 * variables[0] ** 2 + -10 * variables[0] - 4
            case 2:
                return variables[0] ** 3 * variables[1] ** 3 - 2 * variables[0] ** 2
            case 3:
                function = bf.Hypersphere
                return function(variables)
            case 4:
                function = bf.Hyperellipsoid()
                return function(variables)
            case 5:
                function = bf.Schwefel
                return function(variables)
            case 6:
                function = bf.Ackley
                return function(variables)
            case 7:
                function = bf.Michalewicz
                return function(variables)
            case 8:
                function = bf.Rastrigin
                return function(variables)
            case 9:
                function = bf.Rosenbrock
                return function(variables)
            case 10:
                function = bf.DeJong3
                return function(variables)
            case 11:
                function = bf.DeJong5
                return function(variables)
            case 12:
                function = bf.MartinGaddy
                return function(variables)
            case 13:
                function = bf.Griewank
                return function(variables)
            case 14:
                function = bf.Easom
                return function(variables)
            case 15:
                function = bf.GoldsteinAndPrice
                return function(variables)
            case 16:
                function = bf.PichenyGoldsteinAndPrice
                return function(variables)
            case 17:
                function = bf.StyblinskiTang
                return function(variables)
            case 18:
                function = bf.McCormick
                return function(variables)
            case 19:
                function = bf.Rana
                return function(variables)
            case 20:
                function = bf.EggHolder
                return function(variables)
            case 21:
                function = bf.Keane
                return function(variables)
            case 22:
                function = bf.Schaffer2
                return function(variables)
            case 23:
                function = bf.Himmelblau
                return function(variables)
            case 24:
                function = bf.PitsAndHoles
                return function(variables)


    @staticmethod
    def chromosome_decode(range_start: float, range_end: float, chromosome: Chromosome) -> int:
        return range_start + chromosome.gene_decoded * (range_end - range_start) / (2 ** Chromosome.size - 1)

    def display(self):
        for i in range(0, len(self.chromosome)):
            print(self.chromosome[i].gene, end="    ")
            print(self.chromosome_values[i])
        print(f"Wartosc fitness_function: {self.fitness_function_value}")


class Population:

    def __init__(self, individual_amount: int, variables_amount: int, func_type: int):
        self.individual_amount: int = individual_amount
        self.individuals = []
        self.variables_amount = variables_amount
        self.func_type = func_type

    def add_individual(self, new_individual: Individual):
        self.individuals.append(new_individual)

    def get_func_type(self) -> int:  # Metoda zwracająca wartość func_type
        return self._func_type

