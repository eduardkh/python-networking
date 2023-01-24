package main

import (
	"fmt"

	"github.com/scrapli/scrapligo/driver/generic"
	"github.com/scrapli/scrapligo/driver/options"
)

func main() {
	d, err := generic.NewDriver(
		"192.168.143.170",
		options.WithAuthNoStrictKey(),
		options.WithSSHConfigFile("~/.ssh/config"),
		options.WithAuthUsername("cisco"),
		options.WithAuthPassword("cisco"),
	)
	if err != nil {
		fmt.Printf("failed to create driver; error: %+v\n", err)

		return
	}

	err = d.Open()
	if err != nil {
		fmt.Printf("failed to open driver; error: %+v\n", err)

		return
	}
	defer d.Close()

	// fetch the prompt
	prompt, err := d.GetPrompt()
	if err != nil {
		fmt.Printf("failed to get prompt; error: %+v\n", err)

		return
	}

	fmt.Printf("found prompt: %s\n\n\n", prompt)

	// // send some input
	// output, err := d.Channel.SendInput("show run")
	// if err != nil {
	// 	fmt.Printf("failed to send input to device; error: %+v\n", err)

	// 	return
	// }

	// fmt.Printf("output received (SendInput):\n %s\n\n\n", output)

	// // send an interactive input
	// // SendInteractive expects a slice of `SendInteractiveEvent` objects
	// events := make([]*channel.SendInteractiveEvent, 2)
	// events[0] = &channel.SendInteractiveEvent{
	// 	ChannelInput:    "clear logging",
	// 	ChannelResponse: "[confirm]",
	// 	HideInput:       false,
	// }
	// events[1] = &channel.SendInteractiveEvent{
	// 	ChannelInput:    "",
	// 	ChannelResponse: "#",
	// 	HideInput:       false,
	// }

	// // note that there is a convenience wrapper around send interactive in the generic driver as
	// // well, so you could simply do `d.SendInteractive` here rather than poking the channel directly
	// // remember to refer to `.Result` object in that case
	// interactiveOutput, err := d.Channel.SendInteractive(events)
	// if err != nil {
	// 	fmt.Printf("failed to send interactive input to device; error: %+v\n", err)

	// 	return
	// }

	// fmt.Printf("output received (SendInteractive):\n %s\n\n\n", interactiveOutput)

	// send a command -- as this is a "base" driver (meaning there is no context of the type of
	// device we are connecting to) there will have been no paging disabling, so have to
	// either disable paging yourself or send a command that will not make the device page the
	// output!
	r, err := d.SendCommand("show run")
	if err != nil {
		fmt.Printf("failed to send command; error: %+v\n", err)
		return
	}
	if r.Failed != nil {
		fmt.Printf("response objects indicates failure: %+v\n", r.Failed)
		return
	}

	fmt.Printf(
		"sent command '%s', output received (SendCommand):\n %s\n\n\n",
		r.Input,
		r.Result,
	)
}
