	function setHardwareOptions(id){
			// id is the main div id containing hardware.html
			$(id+" #hardware-interfaces").find('option').remove();
			$(id+" #hardware-graphics").find('option').remove();
            $(id+" #hardware-videos").find('option').remove();
            $(id+" #hardware-boots").find('option').remove();
            $(id+" #hypervisors_pools").find('option').remove();
            
			api.ajax_async('/hardware','GET','').done(function(hardware) {
                // Needs a hidden input to activate disabled dropdowns...
                //~ if(hardware.nets.length==1){$(id+" #hardware-interfaces").prop('disabled',true);}
				$.each(hardware.nets,function(key, value) 
				{
					$(id+" #hardware-interfaces").append('<option value=' + value.id + '>' + value.name + '</option>');
				});
                
				//~ if(hardware.graphics.length==1){$if(hardware.nets.length==1){$(id+" #hardware-interfaces").prop('disabled',true);}(id+" #hardware-graphics").prop('disabled',true);}
				$.each(hardware.graphics,function(key, value) 
				{
					$(id+" #hardware-graphics").append('<option value=' + value.id + '>' + value.name + '</option>');
				});
                
                //~ if(hardware.videos.length==1){$(id+" #hardware-videos").prop('disabled',true);}
				$.each(hardware.videos,function(key, value) 
				{
					$(id+" #hardware-videos").append('<option value=' + value.id + '>' + value.name + '</option>');
				});
                
                //~ if(hardware.boots.length==1){$(id+" #hardware-boot_order").prop('disabled',true);}
				$.each(hardware.boots,function(key, value) 
				{
					$(id+" #hardware-boot_order").append('<option value=' + value.id + '>' + value.name + '</option>');
				});
                
                //~ if(hardware.hypervisors_pools.length==1){$(id+" #hypervisors_pools").prop('disabled',true);}
				$.each(hardware.hypervisors_pools,function(key, value) 
				{   // hypervisors_pools is not inside hardware (take it into account when editing!)
					$(id+" #hypervisors_pools").append('<option value=' + value.id + '>' + value.name + '</option>');
				});
				$(id+" #hardware-memory").ionRangeSlider({
						  type: "single",
						  min: 500,
						  max: hardware.user['quota-hardware-memory']/1000,
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");
				$(id+" #hardware-vcpus").ionRangeSlider({
						  type: "single",
						  min: 1,
						  max: hardware.user['quota-hardware-vcpus'],
						  grid: true,
						  disable: false
						  }).data("ionRangeSlider");		
			}); 
	}

	function setHardwareDomainDefaults(div_id,domain_id){
			// id is the domain id
            $(div_id+' #hardware-interfaces option:selected').prop("selected", false);
            $(div_id+' #hardware-graphics option:selected').prop("selected", false);
            $(div_id+' #hardware-videos option:selected').prop("selected", false);
            $(div_id+' #hardware-boot_order option:selected').prop("selected", false);
            $(div_id+' #hypervisors_pools option:selected').prop("selected", false);
            
			api.ajax('/domain','POST',{'pk':domain_id}).done(function(domain) {
				$(div_id+' #hardware-interfaces option[value="'+domain['hardware-interfaces'][0].id+'"]').prop("selected",true);
				$(div_id+' #hardware-graphics option[value="'+domain['hardware-graphics-type']+'"]').prop("selected",true);
                $(div_id+' #hardware-videos option[value="'+domain['hardware-video-type']+'"]').prop("selected",true);
                $(div_id+' #hardware-boot_order option[value="'+domain['hardware-boot_order'][0]+'"]').prop("selected",true);
                $(div_id+' #hypervisors_pools option[value="'+domain['hypervisors_pools'][0]+'"]').prop("selected",true);
				$(div_id+" #hardware-memory").data("ionRangeSlider").update({
						  from: domain['hardware-memory']/1000
                });
				$(div_id+" #hardware-vcpus").data("ionRangeSlider").update({
						  from: domain['hardware-vcpus']
                });
					  
			}); 
	}

	function setHardwareDomainDefaults_viewer(div_id,domain_id){
			api.ajax('/domain','POST',{'pk':domain_id,'hs':true}).done(function(domain) {
				$(div_id+" #vcpu").html(domain['hardware-vcpus']+' CPU(s)');
				$(div_id+" #ram").html(domain['hardware-memory']);
                // List could not be ordered! In theory all the disks have same virtual-size
                $(div_id+" #disks").html(domain['disks_info'][0]['virtual-size']);
				$(div_id+" #net").html(domain['hardware-interfaces'][0].id);
				$(div_id+" #graphics").html(domain['hardware-graphics-type']);
                $(div_id+" #video").html(domain['hardware-video-type']);
                $(div_id+" #boot").html(domain['hardware-boot_order']);
                $(div_id+" #hypervisor_pool").html(domain['hypervisors_pools'][0]);
			}); 
	}

    function setHardwareGraph() {
        // Not implemented
    }

