chai.should();
 
describe('get_latlong', function() {
    beforeEach(function() {
        this.xhr = sinon.useFakeXMLHttpRequest();
     
        this.requests = [];
        this.xhr.onCreate = function(xhr) {
          this.requests.push(xhr);
        }.bind(this);
    });
    
    afterEach(function() {
    this.xhr.restore();
    });

    
});