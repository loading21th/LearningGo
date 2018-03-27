	function updatemoney(is_add,campusid=0)
    {
        var money_update_sum = 0;
        var form_data = new FormData();
        var urlpath = '';
        if (is_add == "yes")
        {
            money_update_sum = document.getElementById('money_add_sum').value;
            urlpath='/LearningGo/userinfo/wallet';
        }
        else if (is_add == "no")
        {
            money_update_sum = document.getElementById('money_del_sum').value;
            urlpath='/LearningGo/userinfo/wallet';
        }
        else if (is_add == "createcampus")
        {
            money_update_sum = document.getElementById('money_buy_campus').value;
            urlpath='/LearningGo/userinfo/buycreatecampus/';
        }
        else if (is_add == "createclass")
        {
            money_update_sum = document.getElementById('money_buy_class').value;
            urlpath='/LearningGo/userinfo/buycreateclass';
            form_data.append("campusid",campusid);
        }
        form_data.append("money_update_sum",money_update_sum);
        form_data.append("is_add",is_add);
        $.ajax({
            type:'POST',
            url :urlpath,
            data:form_data, 
            contentType:false,
            processData:false,
            mimeType:"multipart/form-data",
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = JSON.parse(arg).status;
                if(val == 'success')
                {
                    window.location.href=('/LearningGo/userinfo/teacher');
                }else{
                    alert(val);
                }
   	        }
        });
    }
	function can_createcampus()
    {
        $.ajax({
            type:'GET',
            url :'/LearningGo/userinfo/buycreatecampus',
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = arg["status"];
                if(val == "success")
                {
                    $("#createnewcampus").modal("show");
                }else{
                    $("#buy_createcampus").modal("show");
                }
   	        }
        });
    }
	function can_createclass(campusid)
    {
        var cont = {"campusid":campusid}
        $.ajax({
            type:'GET',
            url :'/LearningGo/userinfo/buycreateclass',
            data:cont,
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = arg["status"];
                if(val == "success")
                {
                    $("#createnewclass").modal("show");
                }else{
                    $("#buy_createclass").modal("show");
                }
   	        }
        });
    }
	function createnewcampus()
    {
        var form_data = new FormData();
        var name = document.getElementById("campus_name").value;
        var abbr = document.getElementById("campus_abbr").value;
        var stage = document.getElementById("campus_stage").value;
        var pupose = document.getElementById("campus_pupose").value;
        var bio = document.getElementById("campus_bio").value;
        var logo = document.getElementById("campus_logo").files[0];
        form_data.append("name",name);
        form_data.append("abbr",abbr);
        form_data.append("stage",stage);
        form_data.append("pupose",pupose);
        form_data.append("bio",bio);
        form_data.append("logo",logo);
        $.ajax({
            type:'POST',
            url :'/LearningGo/userinfo/addcampus',
            data:form_data, 
            contentType:false,
            processData:false,
            mimeType:"multipart/form-data",
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = JSON.parse(arg).status;
                if(val == 'success')
                {
                    window.location.href=('/LearningGo/userinfo/teacher');
                }else{
                    alert('建校失败');
                }
   	        }
        });
    }
	function createnewclass(campusid)
    {
        var form_data = new FormData();
        var name = document.getElementById("class_name").value;
        var abbr = document.getElementById("class_abbr").value;
        var stage = document.getElementById("class_stage").value;
        var bio = document.getElementById("class_bio").value;
        var time = document.getElementById("class_time").value;
        var price = document.getElementById("class_price").value;
        var logo = document.getElementById("class_logo").files[0];
        form_data.append("name",name);
        form_data.append("abbr",abbr);
        form_data.append("stage",stage);
        form_data.append("bio",bio);
        form_data.append("time",time);
        form_data.append("price",price);
        form_data.append("logo",logo);
        $.ajax({
            type:'POST',
            url :'/LearningGo/userinfo/asscampus',
            data:form_data, 
            contentType:false,
            processData:false,
            mimeType:"multipart/form-data",
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = JSON.parse(arg).status;
                alert(val);
                window.location.href=('/LearningGo/campus/manage/'+campusid);
   	        }
        });
    }
	function manageCampus()
    {
        var campusid = (this).id;
        var cont = {"campusid":campusid}
        $.ajax({
            type:'GET',
            url :'/LearningGo/campus/manage',
            data:cont,
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = arg["status"];
                if(val == "success")
                {
                    $("#createnewclass").modal("show");
                }else{
                    $("#buy_createclass").modal("show");
                }
   	        }
        });
    }
	function update_info()
    {
        var form_data = new FormData();
        var name = document.getElementById('uname').value;
        var email = document.getElementById('uemail').value;
        var birth = document.getElementById('ubirth').value;
        var sex = document.getElementById('usex').value;
        var imageNode = document.getElementById('uimage');
        if(imageNode.value!="")
        {
            var image = imageNode.files[0];
            form_data.append("image",image);
        }
        form_data.append("name",name);
        form_data.append("email",email);
        form_data.append("birth",birth);
        form_data.append("sex",sex);
        $.ajax({
            type:'POST',
            url :'/LearningGo/userinfo/teacher',
            data:form_data, 
            contentType:false,
            processData:false,
            mimeType:"multipart/form-data",
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = JSON.parse(arg).status;
                if(val == 'success')
                {
                    window.location.href=('/LearningGo/userinfo/teacher');
                }else{
                    alert('修改信息失败');
                }
   	        }
        });
    }
