_satellite.pushAsyncScript(function(event, target, $variables){
  _satellite.notify('userInfo',1);
_satellite.setVar('userID', event.detail.userID);
_satellite.setVar('loggedIn', event.detail.loggedIn);
_satellite.setVar('vip', event.detail.vip);
_satellite.setVar('over13', event.detail.over13);

_satellite.notify('over13',_satellite.getVar('over13'));

checkDecible(_satellite.getVar('over13'));
});
