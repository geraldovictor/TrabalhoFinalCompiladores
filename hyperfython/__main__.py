from hyperfython import parser

while True:
    text = input('hyperfython >')
    result, error = parse(text)

    if error: print(error.as_string())
    else: print(result)

if __name__ == '__main__':
    main()