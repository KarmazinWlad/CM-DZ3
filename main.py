from src.utils.errors import ConfigurationError
from src.utils.generator import generate_output
from src.utils.parser import parse_xml, parse_name

const = {}

def type(data):
    if data:
        if ('@"' == data[:2] and '"' == data[-1]):
            return data[2:-1]
        elif ('"!' == data[:2] and '"' == data[-1]):
            return const[data.replace("\"", "").replace("![", "").replace("]", "")]
        elif ("({" == data.replace("\"(", "(")[:2] and "})" == data.replace(")\"", ")")[-2:]):
            data = data.replace("\"(", "(").replace(")\"", ")")[2:-2]
            start = 0
            slovo = ""
            fold = []
            for g in data:

                if g == "(":
                    start += 1
                if not start and g == ",":
                    fold.append(slovo)
                    slovo = ""
                else:
                    slovo += g
                if g == ")":
                    start -= 1
            fold.append(slovo)
            a = []
            for newdata in fold:
                a.append(type(newdata))
            return a
        else:
            try:
                return int(data.replace("\"", ""))
            except ValueError:
                None
            try:
                return float(data.replace("\"", ""))
            except ValueError:
                None
            raise ConfigurationError(f"Invalid type variable:{data}")
        return

def load(s):
    slov = {}
    s = s.replace(", ", ",")
    s = s.replace("<configuration>", "").replace("</configuration>", "").replace("<variable","").replace("/>", "")
    arr = s.split('\n')
    comment = ""
    com = "comment"
    for line in arr:
        if (line):
            if ("{{!--" in line and comment == ""):
                comment += line.replace("{{!--", "\"\"\"") + "\n"
                if ("--}}" in line):
                    slov["comment"] = comment.replace("--}}", "\"\"\"")
                    comment = ""
                else:
                    comment+="\n"
            elif ("--}}" in line and comment != ""):
                comment += line.replace("--}}", "\"\"\"")
                slov[f"{com}"] = comment
                com += "."
                comment = ""
            elif (comment != ""):
                comment += line + "\n"
            else:
                elements = []
                list(map(lambda x: elements.append(x) if x !="" and x != "=" else None, line.replace("\'","").split(" ")))
                if(len(elements) > 1):
                    if(elements[0] == "var"):
                        const[parse_name(elements[1])] = type(f'{elements[2]}')
                    elif(type(elements[1].replace("value=", ""))):
                        slov[elements[0].replace("name=", "").replace('"', "")] = type(elements[1].replace("value=", ""))
    print(slov)
    return slov

def main():
    xml_file_path = input("Введите путь к XML-файлу: ")

    try:
        # Открываем файл по указанному пути
        with open(xml_file_path, 'r', encoding="UTF-8") as file:
            s = file.read()
            xml_data = load(s)

        if xml_data is None:
            raise ConfigurationError(f"Configuration error: Invalid value type: {type(xml_data)}")

        # Парсим XML и генерируем выходной формат
        parsed_data = parse_xml(xml_data)
        output = generate_output(parsed_data)
        print("Сконвертированный текст в учебном конфигурационном языке:")
        print(output)


    except FileNotFoundError:
        print(f"Error: File '{xml_file_path}' not found.")
    except ConfigurationError as e:
        print(f"Configuration error: {e}")


if __name__ == "__main__":
    main()
