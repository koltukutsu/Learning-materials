from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit


def main():
    solver = pywraplp.Solver.CreateSolver("GLOP")
    
    x =  solver.NumVar(0, 1, 'x')
    y = solver.NumVar(0, 2, 'y')
    
    # 0 <= 1*x + 1*y <= 2
    ct = solver.Constraint(0, 2, "ct")
    ct.SetCoefficient(x, 1)
    ct.SetCoefficient(y, 1)
    
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 1)
    objective.SetMaximization()
    
    solver.Solve()
    
    print("Solution")
    print("Objective value =", objective.Value())
    print("X = ", x.solution_value())
    print("Y = ", y.solution_value())
    

if __name__ == "__main__":
    pywrapinit.CppBridge.InitLogging("first_tryOR.py")
    cpp_flags = pywrapinit.CppFlags()
    cpp_flags.logtostder = True
    cpp_flags.log_prefix = False
    pywrapinit.CppBridge.SetFlags(cpp_flags)
    
    main()
    