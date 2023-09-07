from challenge_3 import brute_force


def brute_force_list(list_string):
    matrix = []
    for i in range(0, len(list_string)):
        string = list_string[i].rstrip()
        possible_winner = brute_force(string)
        matrix.append({
            'position': i,
            'key' : possible_winner['key'],
            'plaintext': possible_winner['plaintext'],
            'score': possible_winner['score']    
        })
    result = sorted(matrix, key=lambda c: c['score'], reverse=True)[0]
    return result

def main(): 
    path = r'C:\Local\vsc\python\cryptopals\challenges\set 1\4.txt'
    with open(path) as f:
        lines = f.readlines()
    output = brute_force_list(lines)
    print(output)

if __name__ == "__main__":
    main()