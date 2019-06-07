





def copytask(request):
    # source = request.GET['src']
    # destination = request.GET['dst']
    # copy_type = request.GET['copy_type']
    # print(source,destination,copy_type)
    # rets = {"source":source,'target':destination}
    # retsj = json.dumps(rets) #返回json类型数据 {"source": "/mnt/source1/qin.txt", "target": "/mnt/target1/qin.txt"}


    json_list = {}
    json_list["name"] = 'haha'
    json_list["sex"] = 'ssssseeeeexxxxx'




    from django.http import HttpResponse
    import json
    print(json_list)
    return HttpResponse(json.dumps(json_list),content_type="application/json")

