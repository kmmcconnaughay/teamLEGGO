_satellite.pushAsyncScript(function(event, target, $variables){
  adobe.target.getOffer({
  "mbox": "target-global-mbox",
  "params": {
    "pageType" : _satellite.getVar("pageType")
  },
  "success": function(offer) {
    adobe.target.applyOffer({
      offer: offer
    });
  },
  "error": function(status, error) {
    console.log(error)
  }
});
});
