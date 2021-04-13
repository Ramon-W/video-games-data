$(document).ready(function(){
	var json = [{"Title": "Super Mario"}];
		$('#txt-search').keyup(function(){
			var searchField = $(this).val();
			if(searchField === '')  {
				$('#filter-records').html('');
				return;
			}
			var regex = new RegExp(searchField, "i");
			var output = '<div class="row">';
			var count = 1;
			$.each(json, function(key, val){
				if ((val.Title.search(regex) != -1) || (val.employee_name.search(regex) != -1)) {
					output += '<div class="col-md-6 well">';
					output += '<div class="col-md-7">';
				        output += '<h5>' + val.Title + '</h5>';
				  	output += '</div>';
				  	output += '</div>';
				  	if(count%2 == 0){
						output += '</div><div class="row">'
					}
					count++;
				}
			});
			output += '</div>';
			$('#filter-records').html(output);
		});
	});
