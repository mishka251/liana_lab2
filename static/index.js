//let enabled_types = ['C', 'F', 'K'];
$(document).ready(function(){
    let $form = $('#main');
   $form.on('submit', function(event){
       event.preventDefault();
       let data = $form.serialize();
       $.ajax({
           url:'calc/',
           data:data,
           method:'GET',
           success:function(response){
               console.log(response);
               $('.result-box').text('Результат = '+response.outputValue);
           }
       })
   })
});

//
// window.onload = function (event) {
//     let vue_app = new Vue({
//         el: '#vue-app',
//         data: {
//             test: 'hello',
//             types: enabled_types,
//             selectedInputType: enabled_types[0],
//             selectedOutputType: null,
//             input_value: null,
//             result:'',
//         },
//         methods: {
//              get_result: function () {
//                 console.log('calcuating');
//                 if (this.selectedOutputType) {
//
//                     let url = new URL(location.href + 'calc/');
//
//                     let params = {
//                         'inputValue': this.input_value,
//                         'inputType': this.selectedInputType,
//                         'outputType': this.selectedOutputType,
//                     };
//                     for (let key in params) {
//                         url.searchParams.append(key, params[key]);
//                     }
//
//                       axios.get(url).then((response) => {
//                             console.log(response);
//                             this.result= response.data.outputValue;
//                         }
//                         //   return
//                     ).catch(function (error) {
//                         console.log( Promise.reject(error.status));
//                     });
//                 }
//             }
//         }
//
//     });
// };