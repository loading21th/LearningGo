	function updatemoney(is_add)
    {
        var money_update_sum = 0;
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
            urlpath='/LearningGo/userinfo/buycreatecampus';
        }
        else if (is_add == "createclass")
        {
            money_update_sum = document.getElementById('money_buy_class').value;
            urlpath='/LearningGo/userinfo/buycreateclass';
        }
        var yue = document.getElementById('yue').value;
        var form_data = new FormData();
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
	function can_createclass()
    {
        var campus_name = (this).parentNode.getElementById('campus_name').value;
        var cont = {"campus_name":campus_name}
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
	function createnewclass()
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
   	        }
        });
    }
