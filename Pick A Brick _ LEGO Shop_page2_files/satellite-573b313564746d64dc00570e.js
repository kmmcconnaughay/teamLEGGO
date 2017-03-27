_satellite.pushAsyncScript(function(event, target, $variables){
  //Set Environment
var env = _satellite.getVar("isTrackmanProd");
_satellite.notify('initSite',1);
// Trackman callback
var callTrackmanBacklog = undefined;
window.callTrackman = function callTrackman(callback) {

  if (window.TrackMan) {
    if (callTrackmanBacklog != undefined) {
      var callThisFirst = callTrackmanBacklog;
      callTrackmanBacklog = undefined;
      window.callTrackman(callThisFirst);
      _satellite.notify("Cleared Trackman backlog",2);
//      window.alert("Cleared Trackman backlog");
    }
    if (callback) {
//      window.alert("Calling now");
      TrackMan.useModule(
        [TrackMan.Modules.ShopTracking, TrackMan.Modules.BasicTracking, TrackMan.Modules.SearchTracking],
        function(shopTracking, basicTracking, searchTracking) {
          try {
            callback(shopTracking, basicTracking, searchTracking);
          } catch (e) {
            _satellite.notify(e, 5);
          }
        });
    }
  } else {
//      window.alert("Seeing if something to add to backlog"+callback);
    if (callback != undefined) {
//      window.alert("Add to Trackman backlog");
      _satellite.notify("Add to Trackman backlog",2);
      callTrackmanBacklog = callback; // Only keep one, so doesn't grow indefinitely
    }
  }
};

  (function(d) {
    var tk = d.createElement('script');
    //tk.setAttribute('data-tracking-script','trackman.js');
    tk.src = getTrackmanEnvironmentScript(env);
    tk.type = 'text/javascript';
    tk.async = 'true';
    tk.onload = tk.onreadystatechange = function() {
      
      var rs = this.readyState;
      if (rs && rs != 'complete' && rs != 'loaded') return;
      try {
          window.callTrackman(function(shopTracking, basicTracking){
            
						_satellite.notify('setContentCulture',1);
            basicTracking.setContentCulture(_satellite.getVar('currentLocale'));
            shopTracking.setShipToCountry(_satellite.getVar('currentCountry'));
          });
    			window.callTrackman();
        
      } catch (e) {
        _satellite.notify(e);
      }
    };
    var s = d.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(tk, s);
    if(event.detail.callback) {
    	event.detail.callback();
    }
  })(document);

window.trackmanDeepCopy = function (o) {
  // Because trackman alters objects sent in, need to deep copy first
  return JSON.parse( JSON.stringify(o) );
};
});
