
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
        else if (is_add == "upgrade")
        {
            money_update_sum = document.getElementById('money_pay_sum').value;
            urlpath='/LearningGo/userinfo/buyupgrade';
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
                    window.location.href=('/LearningGo/userinfo/student');
                }else{
                    alert(val);
                }
   	        }
        });
    }
	function can_upgrade()
    {
        $.ajax({
            type:'GET',
            url :'/LearningGo/userinfo/buyupgrade',
            error:function()
            {
                alert('请求失败');
            },
            success:function(arg)
            {
				val = arg["status"];
                if(val == "success")
                {
                    $("#upgrade").modal("show");
                }else{
                    $("#zhifu").modal("show");
                }
   	        }
        });
    }
	function upgradeinfo()
    {
        var form_data = new FormData();
        var descripition = document.getElementById("descripition").value;
        var Go_credential = document.getElementById("Go_credential").files[0];
        var teach_credential = document.getElementById("teach_credential").files[0];
        form_data.append("descripition",descripition);
        form_data.append("Go_credential",Go_credential);
        form_data.append("teach_credential",teach_credential);
        $.ajax({
            type:'POST',
            url :'/LearningGo/userinfo/upgradeinfo',
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
                    alert('升级失败');
                }
   	        }
        });
    }
