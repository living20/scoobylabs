import pandas as pd

def get_user_inputs():
    parts_data = []
    n_parts = int(input("Enter the number of parts: "))
    for _ in range(n_parts):
        part_name = input("Enter part name: ")
        quantity = int(input(f"Enter quantity for {part_name}: "))
        n_operations = int(input(f"Enter the number of operations for {part_name}: "))
        operations = []
        for i in range(n_operations):
            machine = input(f"Enter machine name for operation {i+1}: ")
            time = int(input(f"Enter operation time on {machine} in minutes: "))
            operations.append({'machine': machine, 'time': time})
        parts_data.append({'part': part_name, 'quantity': quantity, 'operations': operations})
    parts_df = pd.DataFrame(parts_data)
    parts_df.to_pickle('parts_data.pkl')
    return parts_df

if __name__ == "__main__":
    parts_df = get_user_inputs()
    print(parts_df)
