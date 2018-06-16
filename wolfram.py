import wolframalpha
import config

client = wolframalpha.Client(config.key)

# res = client.query("sin(x) + 2 cos(x) = -1")
keyword = "solution"

def wolfram_req(equation):
    res = client.query(equation)
    if int(res["@numpods"]) == 0:
        return ""
    pods_list = list(res.pods)
    for pod in pods_list:
        if keyword in pod["@title"].lower():
            ans = []
            print(pod)
            if int(pod["@numsubpods"]) > 1:
                for subpod in pod["subpod"]:
                    ans.append(subpod["img"]["@src"])
            elif int(pod["@numsubpods"]) > 0:
                img = pod["subpod"]["img"]["@src"]
                ans.append(img)
            return ans
    return ""