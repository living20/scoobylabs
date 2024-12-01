from ortools.sat.python import cp_model
import pandas as pd

def schedule_operations(parts_df):
    model = cp_model.CpModel()
    tasks = {}
    horizon = 0

    for idx, row in parts_df.iterrows():
        part = row['part']
        quantity = row['quantity']
        operations = row['operations']
        for op_idx, op in enumerate(operations):
            machine = op['machine']
            duration = op['time'] * quantity
            start_var = model.NewIntVar(0, 1000, f'start_{part}_{machine}_{op_idx}')
            end_var = model.NewIntVar(0, 1000, f'end_{part}_{machine}_{op_idx}')
            interval = model.NewIntervalVar(start_var, duration, end_var, f'interval_{part}_{machine}_{op_idx}')
            tasks[(part, op_idx)] = (start_var, end_var, interval)
            horizon += duration

    makespan = model.NewIntVar(0, horizon, 'makespan')
    model.Minimize(makespan)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Optimal schedule found with makespan: {solver.Value(makespan)}")
        for key, (start_var, end_var, _) in tasks.items():
            part, op_idx = key
            print(f"Part {part} - Operation {op_idx} starts at {solver.Value(start_var)} and ends at {solver.Value(end_var)}")
    else:
        print("No optimal solution found.")

if __name__ == "__main__":
    parts_df = pd.read_pickle('parts_data.pkl')
    schedule_operations(parts_df)
