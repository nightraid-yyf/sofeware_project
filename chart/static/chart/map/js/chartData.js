//-------------------------myChart1的更新------------------------------------
var deversion1
$(function(){
    
  
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myChart1",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    if (result) {
        var version = result[0].version
         for(var i=1;i<result.length;i++){       
            option.series[i].data=result[i].data
        }
         myChart1.hideLoading();  
         myChart1.clear();
         myChart1.setOption(option,true);
    }
    deversion1 = version
  },
  error : function(errorMsg) {
    //请求失败时执行该函数
  alert("无法请求数据");
  myChart1.hideLoading();
  }
  })
});

setInterval(function(){   
  
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myChart1",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    if (result) {
         version = result[0].version
         
        if(version != deversion1){
         deversion1 = version
         for(var i=1;i<result.length;i++){       
          option.series[i].data=result[i].data
      }
         myChart1.hideLoading();  
         myChart1.clear();
         myChart1.setOption(option,true);}
    }
  
  },
  error : function(errorMsg) {
    //请求失败时执行该函数
  alert("无法请求数据");
  myChart1.hideLoading();
  }
  })
  },10000);


//-------------------------myChart3的更新------------------------------------
  var deversion3
$(function(){
var srcData3=[];     
  
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myChart3",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    if (result) {
      var version = result[0].version
       for(var i=1;i<result.length;i++){       
        srcData3.push({
          value: result[i].value,
          name: result[i].name
      });
    }
    option3.series[0].data=srcData3;
    option3.series[1].data=srcData3;
    myChart3.hideLoading();  
    myChart3.clear();
    myChart3.setOption(option3,true);
    }
    deversion3 = version
  },
  error : function(errorMsg) {
    //请求失败时执行该函数
  alert("无法请求数据");
  myChart3.hideLoading();
  }
  })
});

setInterval(function(){
  var srcData3=[];     
  
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myChart3",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    
    if (result) {
         version = result[0].version
         
        if(version != deversion3){
          deversion3 = version
          for(var i=1;i<result.length;i++){       
            srcData3.push({
            value: result[i].value,
            name: result[i].name
             });
           }
        option3.series[0].data=srcData3;
        option3.series[1].data=srcData3;
        myChart3.hideLoading();  
        myChart3.clear();
        myChart3.setOption(option3,true);}
    }
  
  },
  error : function(errorMsg) {
    //请求失败时执行该函数
  alert("无法请求数据");
  myChart3.hideLoading();
  }
  })
  },10000);


  //-------------------------myChart4的更新------------------------------------
var deversion4
$(function(){
var srcData4_1=[];     
var srcData4_2=[]; 
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myChart4",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    if (result){
      var version = result[0].version
       for(var i=1;i<=result[0].length1;i++){       
        srcData4_1.push({
          value: result[i].value,
          name: result[i].name
       });
      }
      for(var i=1;i<=result[0].length2;i++){       
        srcData4_2.push({
          value: result[i+result[0].length1].value,
          name: result[i+result[0].length1].name
       });
      }
    option4.series[0].data=srcData4_1;
    option4.series[1].data=srcData4_2;
    myChart4.hideLoading();  
    myChart4.clear();
    myChart4.setOption(option4,true);
    
    }
    deversion4 = version
  },
  error : function(errorMsg) {
    //请求失败时执行该函数
  alert("无法请求数据");
  myChart4.hideLoading();
  }
  })
});

setInterval(function(){
  var srcData4=[];     
  
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myChart4",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    if (result){
      var version = result[0].version
      if(version!=deversion4){
       for(var i=1;i<=result[0].length1;i++){       
        srcData4_1.push({
          value: result[i].value,
          name: result[i].name
       });
      }
      for(var i=1;i<=result[0].length2;i++){       
        srcData4_2.push({
          value: result[i+result[0].length1].value,
          name: result[i+result[0].length1].name
       });
      }
    option4.series[0].data=srcData4_1;
    option4.series[1].data=srcData4_2;
    myChart4.hideLoading();  
    myChart4.clear();
    myChart4.setOption(option4,true);
      }
    }
    deversion4 = version
  },
  error : function(errorMsg) {
    //请求失败时执行该函数
  alert("无法请求数据");
  myChart4.hideLoading();
  }
  })
  },10000);

