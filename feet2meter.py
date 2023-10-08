def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    a = float(v[:-2])
    m = a*0.3048
    return m
main()