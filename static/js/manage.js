
function SelectInit() {
    console.log('测试初始化下拉框');
    cmbProject = document.getElementById('projectsList');
    cmbModule = document.getElementById('modulesList');

    var dataList = [];

    // 创建下拉框选项
    function addOption(cmb, obj) {
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = obj.name;
        option.value = obj.id;
        console.log("option", option)
    }

    // 调用获取select数据列表
    function getSelectData() {
        $.get("/interface/get_select_data/", {}, function (resp) {
            if(resp.status == 10200) {
                dataList = resp.data;
                //遍历项目
                for (var i=0; i< dataList.length; i++) {
                    console.log("每一个项目的数据", dataList[i]);
                    addOption(cmbProject, dataList[i])
                }
            }
        })
    }
    getSelectData()
}