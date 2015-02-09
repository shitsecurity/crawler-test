% rebase('templates/core/index.tpl')
<h1>Submit</h1>

<form method="POST" action="{{get_url('submit')}}">
	<input type="checkbox" name="checkbox1" value="checkbox1">
	<input type="checkbox" name="checkbox2" value="checkbox2">
	<input type="submit" value="Go">
</form>

<form method="POST" action="{{get_url('submit')}}">
	<input type="text" name="user">
	<input type="password" name="password">
	<input type="hidden" name="hidden" value="hidden">
	<input type="submit" value="Go">
</form>

<form method="POST" action="{{get_url('submit')}}">
	<input type="radio" name="radio1" value="default1">
	<input type="radio" name="radio1" value="other1">
	<input type="radio" name="radio2" value="default2">
	<input type="radio" name="radio2" value="other2">
	<input type="submit" value="Go">
</form>

<form method="POST" action="{{get_url('submit')}}">
	<input type="text" name="null" value="">
	<input type="submit" value="Go">
</form>

<form method="POST" action="{{get_url('submit')}}">
	<input type="text" name="text" value="text">
	<input type="submit" value="Go">
</form>

<form method="POST" action="{{get_url('submit')}}">
	<input type="file" name="file">
	<input type="submit" value="Go">
</form>

<form method="POST" id="select" action="{{get_url('submit')}}">
	<input type="submit" value="Go">
</form>

<select name="select" form="select">
	<option value="" selected>select null</option>
	<option value="select1">select 1</option>
	<option value="select2">select 2</option>
</select>
