# def first_fit(groups, bus_capacity):
#     buses = []  
    
#     for group in groups:
#         placed = False  
        
#         for bus in buses:
#             if bus['remaining'] >= group:
#                 bus['passengers'].append(group)
#                 bus['remaining'] -= group
#                 placed = True
#                 break
        
#         if not placed:
#             buses.append({'passengers': [group], 'remaining': bus_capacity - group})
    
#     return buses

# groups = [3, 1, 6, 4, 5, 2]
# bus_capacity = 7
# result_ff = first_fit(groups, bus_capacity)

# print("First Fit Allocation:")
# for i, bus in enumerate(result_ff):
#     print(f"Bus {i+1}: {bus['passengers']} (Remaining Capacity: {bus['remaining']})")

# def first_fit_decreasing(groups, bus_capacity):
#     sorted_groups = sorted(groups, reverse=True)  
#     return first_fit(sorted_groups, bus_capacity)  

# result_ffd = first_fit_decreasing(groups, bus_capacity)

# print("\nFirst Fit Decreasing Allocation:")
# for i, bus in enumerate(result_ffd):
#     print(f"Bus {i+1}: {bus['passengers']} (Remaining Capacity: {bus['remaining']})")

# from itertools import permutations

# def full_bin_packing(groups, bus_capacity):
#     best_solution = None
#     min_buses = float('inf')

#     for perm in permutations(groups):
#         buses = first_fit(list(perm), bus_capacity)
        
#         if len(buses) < min_buses:
#             min_buses = len(buses)
#             best_solution = buses

#     return best_solution

# result_fbp = full_bin_packing(groups, bus_capacity)

# print("\nFull Bin Packing Allocation:")
# for i, bus in enumerate(result_fbp):
#     print(f"Bus {i+1}: {bus['passengers']} (Remaining Capacity: {bus['remaining']})")

# //Q2
# from itertools import combinations

# def first_fit(departments, capacity):
#     bins = []
#     for dept, strength in departments:
#         placed = False
#         for i in range(len(bins)):
#             if bins[i][0] + strength <= capacity:  
#                 bins[i][0] += strength
#                 bins[i][1].append(dept)
#                 placed = True
#                 break
#         if not placed:
#             bins.append([strength, [dept]])
#     return bins

# def first_fit_decreasing(departments, capacity):
#     sorted_depts = sorted(departments, key=lambda x: x[1], reverse=True)
#     return first_fit(sorted_depts, capacity)

# def full_bin(departments, capacity):
#     depts = departments.copy()
#     bins = []
    
#     exact_matches = []
#     for r in range(1, len(depts) + 1):
#         for combo in combinations(depts, r):
#             total = sum(strength for _, strength in combo)
#             if total == capacity:
#                 exact_matches.append(combo)

#     used_departments = set()
    
#     for combo in exact_matches:
#         bin_strength = sum(strength for _, strength in combo)
#         bin_depts = [dept for dept, _ in combo]
        
#         if not any(dept in used_departments for dept in bin_depts):
#             bins.append([bin_strength, bin_depts])
#             used_departments.update(bin_depts)

#     depts = [d for d in depts if d[0] not in used_departments]

#     remaining_bins = first_fit(depts, capacity)
#     bins += remaining_bins
#     return bins

# departments = [
#     ('A',14), ('B',4), ('C',3), ('D',2), ('E',2),
#     ('F',18), ('G',4), ('H',23), ('I',8), ('J',27),
#     ('K',19), ('L',3), ('M',26), ('N',30), ('O',35), ('P',32)
# ]
# capacity = 50

# ff_bins = first_fit(departments, capacity)
# ffd_bins = first_fit_decreasing(departments, capacity)
# full_bins = full_bin(departments.copy(), capacity)

# def print_bins(bins, algorithm_name):
#     print(f"{algorithm_name} Bins ({len(bins)} buses):")
#     for i, bin in enumerate(bins, 1):
#         print(f"Bus {i}: {bin[1]} (Total: {bin[0]} students)")
#     print()

# print_bins(ff_bins, "First Fit")
# print_bins(ffd_bins, "First Fit Decreasing")
# print_bins(full_bins, "Full Bin Packing")

# Q3
# from ortools.linear_solver import pywraplp
# departments = [
#     ('A',14), ('B',4), ('C',3), ('D',2), ('E',2),
#     ('F',18), ('G',4), ('H',23), ('I',8), ('J',27),
#     ('K',19), ('L',3), ('M',26), ('N',30), ('O',35), ('P',32)
# ]
# capacity = 50
# num_departments = len(departments)
# max_bins = num_departments  
# solver = pywraplp.Solver.CreateSolver("SCIP")
# x = []
# for i in range(num_departments):
#     x.append([solver.BoolVar(f'x[{i},{j}]') for j in range(max_bins)])

# y = [solver.BoolVar(f'y[{j}]') for j in range(max_bins)]

# for i in range(num_departments):
#     solver.Add(sum(x[i][j] for j in range(max_bins)) == 1)

# for j in range(max_bins):
#     solver.Add(sum(x[i][j] * departments[i][1] for i in range(num_departments)) <= capacity * y[j])

# solver.Minimize(solver.Sum(y[j] for j in range(max_bins)))
# status = solver.Solve()
# if status == pywraplp.Solver.OPTIMAL:
#     print("Optimal solution found!\n")
#     used_buses = sum(int(y[j].solution_value()) for j in range(max_bins))
#     print(f"Minimum Buses Required: {used_buses}")
    
#     for j in range(max_bins):
#         if y[j].solution_value() == 1:
#             bus_load = [departments[i][0] for i in range(num_departments) if x[i][j].solution_value() == 1]
#             bus_capacity = sum(departments[i][1] for i in range(num_departments) if x[i][j].solution_value() == 1)
#             print(f"Bus {j+1}: {bus_load} (Total: {bus_capacity} students)")
# else:
#     print("No optimal solution found.")


# # HM 1
# from itertools import combinations
# from collections import Counter

# wire_lengths = [2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 7, 7]
# capacity = 12 

# def first_fit(wires, capacity):
#     bins = []
#     for length in wires:
#         placed = False
#         for bin in bins:
#             if sum(bin) + length <= capacity:
#                 bin.append(length)
#                 placed = True
#                 break
#         if not placed:
#             bins.append([length])
#     return bins

# def first_fit_decreasing(wires, capacity):
#     sorted_wires = sorted(wires, reverse=True)  
#     return first_fit(sorted_wires, capacity)

# def full_bin(wires, capacity):
#     bins = []
#     wire_count = Counter(wires)  

#     for r in range(1, len(wires) + 1):
#         for combo in combinations(wires, r):
#             if sum(combo) == capacity:
#                 temp_count = Counter(combo)  
                
#                 if all(temp_count[key] <= wire_count[key] for key in temp_count):
#                     bins.append(list(combo))
#                     wire_count.subtract(temp_count) 
#     remaining_wires = list(wire_count.elements())  
#     bins.extend(first_fit(remaining_wires, capacity))
    
#     return bins

# ff_bins = first_fit(wire_lengths, capacity)
# ffd_bins = first_fit_decreasing(wire_lengths, capacity)
# full_bin_bins = full_bin(wire_lengths, capacity)

# def print_bins(bins, name):
#     print(f"\n{name} Algorithm - Total Bins: {len(bins)}")
#     for i, bin in enumerate(bins, 1):
#         print(f"Wire {i}: {bin} (Total: {sum(bin)} feet)")

# print_bins(ff_bins, "First Fit")
# print_bins(ffd_bins, "First Fit Decreasing")
# print_bins(full_bin_bins, "Full Bin Packing")

# HM2
# def first_fit(items, bin_capacity):
#     bins = []  

#     for item in items:
#         placed = False  

#         for bin in bins:
#             if sum(bin) + item <= bin_capacity:
#                 bin.append(item)
#                 placed = True
#                 break

#         if not placed:
#             bins.append([item])

#     return bins

# items = [2, 2, 3, 3, 3, 3, 4, 4, 4, 6, 7, 7]  
# bin_capacity = 12  

# bins = first_fit(items, bin_capacity)

# print(f"Total Bins Required: {len(bins)}")
# for i, bin in enumerate(bins, 1):
#     print(f"Bin {i}: {bin} (Total: {sum(bin)} units)")
from ortools.algorithms import pywrapknapsack_solver

def main():
    # Create the solver instance
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample"
    )

    values = [
      360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
      78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
      87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
      312
    ]
    weights = [
      [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
       42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
       3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13],
    ]
    capacities = [850]

    # Initialize and solve
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    # Store packed items and their weights
    packed_items = []
    packed_weights = []
    total_weight = 0
    
    print("Total Value =", computed_value)
    
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    
    print("Total Weight:", total_weight)
    print("Packed Items:", packed_items)
    print("Packed Weights:", packed_weights)

if __name__ == "__main__":
    main()
