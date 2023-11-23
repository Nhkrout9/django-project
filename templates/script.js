function onTrainInputFind(comeFrom) 
{
	var frm= document.frmTRN; 
	frm.target="";
	frm.trainNo.value = trim(frm.trainNo.value);
	var trainNoValue = frm.trainNo.value;
	if(comeFrom == 'K')
	{
		if(trainNoValue.length > 5 && trainNoValue.includes("-"))
		{
			var array = trainNoValue.split("-");
			trainNoValue = array[0];
			frm.trainNo.value = trainNoValue
		}
		
		if(trainNoValue.length == 5 && checkForNumber(trainNoValue) && trainNoValue != '00000')	//5 digit number
		{
			var queryStr = "tr?opt=TrainRunning&subOpt=FindRunningInstance";
			submitForm(frm,queryStr,10);
		}
	}else if(comeFrom == 'A')
	{
		if(trainNoValue.length > 5 && trainNoValue.includes("-"))
		{
			var array = trainNoValue.split("-");
			trainNoValue = array[0];
			frm.trainNo.value = trainNoValue
		}
		
		if(trainNoValue.length == 5 && checkForNumber(trainNoValue) && trainNoValue != '00000')	//5 digit number
		{
			var queryStr = "q?opt=TrainRunning&subOpt=FindStationList";
			submitForm(frm,queryStr,10);
		}else
		{
			showSpot();
		}
	}else if(comeFrom == 'S')
	{
			if(trainNoValue.length > 5 && trainNoValue.includes("-"))
			{
				var array = trainNoValue.split("-");
				trainNoValue = array[0];
				frm.trainNo.value = trainNoValue
			}
			
			if(trainNoValue == '' || trainNoValue == '00000')
			{
				document.getElementById("divMessageText").innerHTML = "Invalid Train No. !!!";
				frm.trainNo.value = '';
				frm.trainNo.focus();
				return false;
			} 
			else if(trainNoValue.length == 5 && checkForNumber(trainNoValue) && trainNoValue != '00000')	//5 digit number
			{
				var queryStr = "tr?opt=TrainRunning&subOpt=FindRunningInstance";
				submitForm(frm,queryStr,10);
			}
			else if(trainNoValue.length == 0 || trainNoValue.length < 3)
			{
				document.getElementById("divMessageText").innerHTML = "Enter Train No./Name [Min. 3 Characters]";
				frm.trainNo.focus();
				return false;
			}
			else if(!checkAlphaNumericSpaceHyphen(trainNoValue) && !checkForNumber(trainNoValue))
			{
				document.getElementById("divMessageText").innerHTML = "Invalid Train No. !!!";
				frm.trainNo.value = '';
				frm.trainNo.focus();
				return false;
			}
			else
			{
				var queryStr = "q?opt=TrainRunning&subOpt=FindTrainS";
				submitForm(frm,queryStr,10);
			}	
		
	}
}


function submitForm(frm,queryStr,waitCnt) {
	fnPleaseWait(waitCnt);
	hideBackContent();
	
	setTimeout(function() {
		frm.action = queryStr;
		frm.submit();
	}, 100);
	/*
	if(queryStr.indexOf("q?type=TrainRunning&subOpt=ShowRunC") != -1) { // In case of train running data only. 
		$.ajax({url:"GetCSRFToken?t=" + new Date().getTime(), success:function(str){
			try {
				var prm = "csrfToken=" + eval(str);
				if(queryStr.indexOf("?") == -1) {
					queryStr += "?" + prm;
				}
				else {
					queryStr += "&" + prm;
				}
				setTimeout(function() {
					frm.action = queryStr;
					frm.submit();
				}, 100);
			} catch(ex){ }
		}, error:function(){alert("Some Error at server side please try again.");}, async:true});
	}
	else {
		setTimeout(function() {
			frm.action = queryStr;
			frm.submit();
		}, 100);
	}*/
}
/* Ends */