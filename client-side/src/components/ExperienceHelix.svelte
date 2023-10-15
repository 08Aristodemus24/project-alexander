<script>
    export let opened;
</script>
<div class="exp-grid-container" class:opened={opened}>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={1}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={2}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={3}>
        <slot name="first-exp"/>
    </div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={4}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={5}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={6}>
        <slot name="second-exp"/>
    </div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={7}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={8}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={9}>
        <slot name="contribs"/>
    </div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={10}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={11}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={12}>
        <slot name="cv"/>
    </div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={13}></div>
    <div class="exp-grid-item" style:--exp-grid-item-animation-order={14}></div>
</div>