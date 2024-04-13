const old = new Date();
const old_sec = old.getSeconds();

var routes = document.querySelectorAll('bus_route')

routes.forEach(function(item){
    let time_O = item.querySelector('.time_O');
    let time_D = item.querySelector('.time_D');
    let bus = item.querySelector('.bus');
    
    if(time_O < time_D){
        let sec_time = time_O * 60;
        const now = new Date();
        const new_sec = now.getSeconds();

        let delta_sec = new_sec - old_sec;
        let dist = sec_time / delta_sec * 0.25;
        bus.computedStyleMap.transform = 'translate('+ dist + ', 0)';
    }
});


