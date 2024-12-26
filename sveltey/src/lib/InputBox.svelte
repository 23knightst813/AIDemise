<script>
    import SuccessMessage from './SuccessMessage.svelte';
    let showMessage = false;

    function handleSubmit(event) {
        event.preventDefault();
        showMessage = true;
        setTimeout(() => showMessage = false, 1000);
    }
</script>

<div>
    <form on:submit={handleSubmit}>
        <input type="text"/>
        <br><br>
        <button type="submit">Submit</button>
    </form>
    <br>
    <SuccessMessage show={showMessage} />
</div>

<style>
    input {
        border: 2px solid #ccc;
        border-radius: 4px;
        padding: 10px;
        font-size: 16px;
        width: 100%;
        box-sizing: border-box;
    }
</style>