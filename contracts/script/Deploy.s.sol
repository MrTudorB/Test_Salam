// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import {Script} from "forge-std/Script.sol";
import {EtherSender} from "../src/EtherSender.sol";
import {console} from "forge-std/console.sol";

contract Deploy is Script {
    function run() external {
        // 1. Start broadcasting with your private key
        vm.startBroadcast();

        // 2. Deploy contract with some initial ETH if desired
        //    e.g., attaching 0.05 ETH so you can test sending 0.01 from it.
        EtherSender etherSender = (new EtherSender){value: 0.05 ether}();

        // 3. Print the deployed address
        console.log("EtherSender deployed at:", address(etherSender));

        // 4. Stop broadcasting
        vm.stopBroadcast();
    }
}
